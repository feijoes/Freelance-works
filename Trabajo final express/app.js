const express = require("express");
const app = express();
const { ErrorHandlerMiddleware, NotFound } = require('./middlewares/middleware')
const productoRouter = require("./routers/ProductoRouter")
const UserRouter = require('./routers/AuthenticationRouter')
const passport = require('passport')
require("./db/Connecion")
require('./config/passport')(passport)


app.use(passport.initialize());
app.use(express.json());
app.use(express.urlencoded({extended:true}))



app.use("/",productoRouter);

// Login Logout and Register
app.use('/',UserRouter);

app.use(NotFound)

app.use(ErrorHandlerMiddleware)

app.listen(5000)