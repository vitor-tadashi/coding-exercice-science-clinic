BEGIN;
    create table cms_medicare
    (
        id serial not null
            constraint id_pkey
            primary key,
        national_provider_identifier integer not null,
        provider_last_organization_name varchar(250) not null,
        provider_first_name varchar(250),
        provider_middle_name varchar(250),
        provider_credentials varchar(50),
        provider_gender char(1),
        entity_type char(1),
        address varchar(250),
        city varchar(150),
        zip_code varchar(20),
        state varchar(3),
        country_code varchar(3),
        geom geometry,
        provider_type varchar(100),
        medicare_participation_indicator char(1),
        service_place char(1),
        hcpcs_code varchar(20),
        hcpcs_description varchar(250),
        hcpcs_drug char(1),
        services smallint,
        medicare_beneficiaries smallint,
        distinct_medicare_beneficiaries smallint,
        average_medicare_allowed_amount numeric(15, 8),
        average_submitted_charge_amount numeric(15, 8),
        average_medicare_payment_amount numeric(15, 8),
        average_medicare_standardized_amount numeric(15, 8)
    );
COMMIT;
