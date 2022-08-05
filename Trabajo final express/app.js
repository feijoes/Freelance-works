const express = require("express");
const app = express();
const { ErrorHandlerMiddleware, NotFound } = require('./middlewares/middleware')
app.use(express.json());


app.use("/api/v1/todo",tasks)

// Login Logout and Register
app.use("/api/v1/",authenticate)

app.use(NotFound)

app.use(ErrorHandlerMiddleware)

app.listen(5000)