with traffic as (

  select * from {{ ref('base_google_analytics_traffic') }}

)

select * from traffic
