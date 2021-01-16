BEGIN;
    create table cms_medicare
    (
        id serial not null
            constraint id_pkey
            primary key,
        national_provider_identifier integer not null,
        provider_last_organization_name varchar(500) not null,
        provider_first_name varchar(500),
        provider_middle_name varchar(500),
        provider_credentials varchar(100),
        provider_gender char(1),
        entity_type char(1),
        address varchar(500),
        address2 varchar(500),
        city varchar(150),
        zip_code varchar(20),
        state varchar(3),
        country_code varchar(3),
        geom geometry,
        provider_type varchar(100),
        medicare_participation_indicator char(1),
        service_place char(1),
        hcpcs_code varchar(20),
        hcpcs_description varchar(500),
        hcpcs_drug char(1),
        services numeric(15, 8),
        medicare_beneficiaries numeric(15, 8),
        distinct_medicare_beneficiaries numeric(15, 8),
        average_medicare_allowed_amount numeric(15, 8),
        average_submitted_charge_amount numeric(15, 8),
        average_medicare_payment_amount numeric(15, 8),
        average_medicare_standardized_amount numeric(15, 8)
    );

    CREATE INDEX index_hcpcs_code ON cms_medicare
    (
        hcpcs_code
    );

    CREATE INDEX index_state ON cms_medicare
    (
        state
    );

    CREATE INDEX index_state_city ON cms_medicare
    (
        state,
        city
    );

    CREATE INDEX cms_medicare_geom_idx
      ON cms_medicare
      USING GIST (geom);

    COPY cms_medicare(national_provider_identifier, provider_last_organization_name,
          provider_first_name, provider_middle_name, provider_credentials, provider_gender,
          entity_type, address, address2, city, zip_code, state, country_code, provider_type,
          medicare_participation_indicator, service_place, hcpcs_code, hcpcs_description,
          hcpcs_drug, services, medicare_beneficiaries, distinct_medicare_beneficiaries,
          average_medicare_allowed_amount, average_submitted_charge_amount,
          average_medicare_payment_amount, average_medicare_standardized_amount)
    FROM '/data/medicare_data.csv'
    DELIMITER ','
    CSV HEADER;

    delete from cms_medicare where city = 'SAN FRANCISCO';

    COPY cms_medicare(national_provider_identifier, provider_last_organization_name,
          provider_first_name, provider_middle_name, provider_credentials, provider_gender,
          entity_type, address, address2, city, zip_code, state, country_code, geom, provider_type,
          medicare_participation_indicator, service_place, hcpcs_code, hcpcs_description,
          hcpcs_drug, services, medicare_beneficiaries, distinct_medicare_beneficiaries,
          average_medicare_allowed_amount, average_submitted_charge_amount,
          average_medicare_payment_amount, average_medicare_standardized_amount)
    FROM '/data/medicare_SF_lat_long_data.csv'
    DELIMITER ','
    CSV HEADER;

COMMIT;
