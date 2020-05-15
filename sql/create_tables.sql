CREATE TABLE lifts (
    lift_id             INTEGER     PRIMARY KEY AUTOINCREMENT,
    title               VARCHAR             NOT NULL,
    current_one_rep_max INTEGER
);

CREATE TABLE metriks(
    id          INTEGER         PRIMARY KEY AUTOINCREMENT,
    timestamp   TIMESTAMP   DEFAULT CURRENT_TIMESTAMP,
    lift_id     INTEGER         NOT NULL,
    reps        INTEGER         NOT NULL,
    weight      INTEGER         NOT NULL,
    intensity   REAL         NOT NULL,

    FOREIGN KEY (lift_id) REFERENCES lift(lift_id)
);