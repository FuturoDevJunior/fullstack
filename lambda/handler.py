def notify_new_order(event, context):
    print("Novo pedido criado:", event)
    return {"statusCode": 200, "body": "Notificação enviada!"}