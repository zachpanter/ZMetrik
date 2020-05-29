CREATE TABLE lifts (
    id             INTEGER     PRIMARY KEY AUTOINCREMENT,
    title               VARCHAR             NOT NULL,
    current_one_rep_max INTEGER
);

CREATE TABLE rauminhalt(
    id          INTEGER         PRIMARY KEY AUTOINCREMENT,
    timestamp   TIMESTAMP   DEFAULT CURRENT_TIMESTAMP,
    lift_id     INTEGER         NOT NULL,
    reps        INTEGER         NOT NULL,
    weight      INTEGER         NOT NULL,
    intensity   REAL         NOT NULL,

    FOREIGN KEY (lift_id) REFERENCES lifts(id)
);

CREATE TABLE morphometriks(
    id          INTEGER         PRIMARY KEY AUTOINCREMENT,
    timestamp   INTEGER         DEFAULT CURRENT_TIMESTAMP,
    metrik_id   INTEGER         NOT NULL,
    amt         REAL,

    FOREIGN KEY (metrik_id) REFERENCES metriks(id)
);

CREATE TABLE metriks(
    id          INTEGER         PRIMARY KEY AUTOINCREMENT,
    title       VARCHAR         NOT NULL,
    unit        VARCHAR         NOT NULL,
);

CREATE TABLE nahrung(
    id          INTEGER         PRIMARY KEY AUTOINCREMENT,
    TIMESTAMP   INTEGER         DEFAULT CURRENT_TIMESTAMP,
    title       VARCHAR,
    eiweiss     INTEGER,
    kalorien    INTEGER
);