Feature: Ingest

    @ingest @daily
    Scenario: Run Daily Ingest
        Given a data ingest job is triggered
        When the Tenant API cron job requests details for all tenants from Prismic
        Then Prismic returns paginated results
        When the Tenant API splits results into threads in batches of 20
        Then for each result, the Tenant API calls "Update Opening Hours" and "Update Search Index"
        Then the Tenant API receives a success response