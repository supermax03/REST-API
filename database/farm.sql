-- Table: farm

-- DROP TABLE farm;

CREATE TABLE farm
(
  name character varying(120) NOT NULL,
  address character varying(120),
  CONSTRAINT farm_pk PRIMARY KEY (name)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE farm
  OWNER TO postgres;
