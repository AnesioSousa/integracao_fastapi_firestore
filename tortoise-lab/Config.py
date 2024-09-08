from tortoise import Tortoise

async def init():
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"
    await Tortoise.init(
        db_url='mysql://admin_ecompjr:EcompJr123#@127.0.0.1/sppe',
        modules={'models': ['app.models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()
