-- upgrade --
ALTER TABLE "citybikestation" RENAME COLUMN "lantitude" TO "latitude";
ALTER TABLE "citybikestation" RENAME COLUMN "status" TO "active";
-- downgrade --
ALTER TABLE "citybikestation" RENAME COLUMN "active" TO "status";
ALTER TABLE "citybikestation" RENAME COLUMN "latitude" TO "lantitude";
