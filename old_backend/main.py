from fastapi import FastAPI

import auth
import home
import profile
import tasks
import team
import messages
import contracts
import clients
import deeds
import payments
import files
import logs

app = FastAPI(title="TMLLAK Backend")

app.include_router(auth.router)
app.include_router(home.router)
app.include_router(profile.router)
app.include_router(tasks.router)
app.include_router(team.router)
app.include_router(messages.router)
app.include_router(contracts.router)
app.include_router(clients.router)
app.include_router(deeds.router)
app.include_router(payments.router)
app.include_router(files.router)
app.include_router(logs.router)
