-- upgrade --
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "citybikestation" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "station_id" INT NOT NULL,
    "name" VARCHAR(100) NOT NULL,
    "status" BOOL NOT NULL,
    "description" TEXT NOT NULL,
    "boxes" INT NOT NULL,
    "free_boxes" INT NOT NULL,
    "free_bikes" INT NOT NULL,
    "longitude" DECIMAL(50,15) NOT NULL,
    "lantitude" DECIMAL(50,15) NOT NULL,
    "internal_id" INT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON TABLE "citybikestation" IS 'The CityBikeStation model';
CREATE TABLE IF NOT EXISTS "address" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "longitude" DECIMAL(50,15) NOT NULL,
    "lontitude" DECIMAL(50,15) NOT NULL,
    "type" VARCHAR(25) NOT NULL,
    "name" VARCHAR(100) NOT NULL,
    "address_id" TEXT NOT NULL,
    "station_id" BIGINT NOT NULL REFERENCES "citybikestation" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "address" IS 'The Address model';
