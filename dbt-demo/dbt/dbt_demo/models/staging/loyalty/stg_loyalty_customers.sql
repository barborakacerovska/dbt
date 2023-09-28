with loyal_customers as (

  select * from {{ source('loyalty', 'loyalty_customers') }}

)

select * from loyal_customers