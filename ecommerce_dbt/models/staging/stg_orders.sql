with source as (
    select * from raw_orders
),
staged as (
    select
        order_id,
        customer_id,
        product_name,
        category,
        quantity,
        unit_price,
        (quantity * unit_price) as total_amount,
        order_date,
        status
    from source
)
select * from staged