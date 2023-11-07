from brushes.models import brush

def bag_contents(request):
    bag = request.session.get('bag', {})
    bag_items = []
    total = 0
    product_count = 0

    for brush_id, quantity in bag.items():
        brush = get_object_or_404(Brush, pk=brush_id)
        item_total = quantity * brush.price
        total += item_total
        product_count += quantity

        bag_items.append({
            'brush_id': brush_id,
            'quantity': quantity,
            'brush': brush,
            'item_total': item_total,
        })

    grand_total = total  

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
