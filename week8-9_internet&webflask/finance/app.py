import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id=session["user_id"]
    stocks=db.execute("SELECT symbol, SUM(shares) as total_shares FROM purchases WHERE user_id=? GROUP BY symbol HAVING total_shares > 0",user_id )

    stockvalue_now = 0
    for stock in stocks:
        quote=lookup(stock["symbol"])
        stock["price"]=quote["price"]
        stock["total"]=stock["total_shares"]*stock["price"]

        stockvalue_now += stock["total"]

    rows=db.execute("SELECT cash FROM users  WHERE id = ?", user_id)
    cash = rows[0]["cash"]

    total_value = cash+stockvalue_now

    return render_template("index.html", stocks=stocks, cash=cash, total=total_value)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol=request.form.get("symbol")
        shares=request.form.get("shares")

        if not symbol:
            return apology("Symbol doesn't exist")

        try:
            shares=int(shares)
            if shares<=0:
                return apology("Please enter a positive integer")
        except ValueError:
            return apology("Please enter a positive integer")

        stock = lookup(symbol)

        if not stock:
            return apology("Stock doesn't exist")

        current_price=stock["price"]
        total_spending=shares*current_price

        user_id=session["user_id"]
        rows=db.execute("SELECT cash FROM users WHERE id = ?",user_id)
        own_cash=rows[0]["cash"]
        if total_spending > own_cash:
            return apology("Can't afford")

        db.execute("UPDATE users SET cash=cash-? WHERE id=?",total_spending, user_id)

        db.execute("INSERT INTO purchases (user_id, symbol, shares, price) VALUES(?, ?, ?, ?)", user_id, symbol, shares, current_price)

        flash("Bought")
        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id=session["user_id"]
    transactions=db.execute("SELECT symbol, price, shares, bought_at FROM purchases WHERE user_id = ? ORDER BY bought_at DESC",user_id)

    return render_template("history.html",transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol=request.form.get("symbol")
        result = lookup(symbol)

        if  not result:
            return apology("NO such quote")

        return render_template("quoted.html", result=result)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        username=request.form.get("username")
        password=request.form.get("password")
        confirmation=request.form.get("confirmation")

        if not username or not password or not confirmation:
            return apology("All fields are required")

        if confirmation != password:
            return apology("Not the same password")

        hash = generate_password_hash(password)

        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)

            rows=db.execute("SELECT id FROM users WHERE username = ?", username)
            session["user_id"] = rows[0]["id"]

            flash("You're registered")
            return redirect("/")

        except ValueError:
            return apology("Repeated User")

    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id=session["user_id"]
    if request.method == "POST":
        shares=request.form.get("shares")
        symbol=request.form.get("symbol")

        if not symbol:
            return apology("Please select a stock")

        try:
            shares=int(shares)
            if shares<=0:
                return apology("Please enter a positive integer")
        except ValueError:
            return apology("Please enter a positive integer")

        rows=db.execute("SELECT SUM(shares) as total FROM purchases WHERE user_id = ? AND symbol = ?",user_id, symbol)
        if not rows or rows[0]["total"] is None:
            return apology("You don't have shares")

        owned=rows[0]["total"]
        if owned < shares:
            return apology("Don't enough")

        stock = lookup(symbol)
        price=stock["price"]
        income=price*shares

        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", income, user_id)
        db.execute("INSERT INTO purchases (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",user_id, symbol, -shares, price)

        return redirect("/")

    else:
        stocks=db.execute("SELECT symbol FROM purchases WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0",user_id)
        return render_template("sell.html",stocks=stocks)
