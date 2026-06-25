with orders as (
    select * from {{ ref('stg_orders') }}
)
select
    category,
    product_name,
    date_trunc('month', order_date) as month,
    count(order_id) as total_orders,
    sum(total_amount) as total_revenue,
    avg(total_amount) as avg_order_value
from orders
where status = 'completed'
group by category, product_name, month
order by month, total_revenue desc
