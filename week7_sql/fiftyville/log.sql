-- Keep a log of any SQL queries you execute as you solve the mystery.

-- to know the basic information about the crime
SELECT description FROM crime_scene_reports
WHERE month = 7 AND day = 28
AND strret = 'Humphrey Street';
/* Theft 10:15 am bakery 3 witnesses* and littering 16:36*/

--Knowing about the witnesses
SELECT transcript, name
FROM interviews
WHERE month = 7 AND day = 28;
/* car in the bakery parking lot 10:25 thief there withdrawing some money.  called someone planning to take the earliest flight out of Fiftyville tomorrow he person on the other end of the phone to purchase the flight ticket.*/

-- see the bakery
SELECT *
FROM bakery_security_logs
WHERE minute * 15 AND day = 28 AND month = 7;
/* HOD8639 exit the parking lot at 10:25*/

--atm transacyion log
SELECT account_number,  transaction_type, id, amount
FROM atm_transactions
WHERE day = 28 AND month = 7 AND year = 2025
AND atm_location = 'Leggett Street';
/*246 264 266 267 269 288 313 336*/

--check the airline
SELECT *
FROM flights
WHERE day = 29 AND month = 7 AND year = 2025;
/* the eariliest filght is 8:20 to 4destination id is 36*/

--check the phone call
SELECT caller, receiver, duration, id
FROM phone_calls
WHERE day = 28 AND month = 7 AND year = 2025;
/* 246 264 266 267 269 not the sus*/

--
SELECT license_plate, activity, minute
FROM bakery_security_logs
WHERE year = 2025 AND month = 7 AND day = 28
AND hour = 10 AND minute BETWEEN 15 AND 25
AND activity = 'exit'
ORDER BY minute;
/*5P2BI95, 94KL13X, 6P58WS2, 4328GD8, G412CB7, L93JTIZ, 322W7JE, 0NTHK55*/

--the people
SELECT name, lincense_plate, id
FROM people
WHERE license_plate in('5P2BI95', '94KL13X', '6P58WS2', '4328GD8', 'G412CB7', 'L93JTIZ', '322W7JE', '0NTHK55');
/*Barry Bruce Diana Iman KELSEY  Luca Sofia Vanessa*/

--check their calls
SELECT caller, receiver, duration
FROM phone_calls
WHERE year = 2025
  AND month = 7
  AND day = 28
  AND duration <= 60
  AND caller IN (
      SELECT phone_number
      FROM people
      WHERE name IN ('Barry', 'Bruce', 'Diana', 'Iman', 'Kelsey', 'Luca', 'Sofia', 'Vanessa')
  );
  /*Sofia Kelsey Bruce Diana*/

  --check the passenger on the flight
  SELECT name
  FROM people
  WHERE passport_number IN(
    SELECT passport_number
    FROM passengers
    WHERE flight_id = 36);
/*Sofia Luca Kelsey Bruce*/

-- where are thry go
SELECT city, full_name
FROM airports
WHERE id = 4;
/*New York City*/

--who the theft call to
SELECT name
FROM people
WHERE phone_number =(
    SELECT receiver
    FROM phone_calls
    WHERE year = 2025
    AND month = 7
    AND day = 28
    AND duration <= 60
    AND caller = (
        SELECT phone_number
        FROM people
        WHERE name = 'Bruce'
        )
);
