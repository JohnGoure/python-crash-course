def car_info(manufacturer, model, **info):
    print(
        "Make: " +
        manufacturer +
        "\nModel: " +
        model +
        "\nAdditional info:" +
        str(info)
        )

car_info('chevy', 'corvette', year='2001', condition='good')
