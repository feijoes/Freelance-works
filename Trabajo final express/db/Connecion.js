require("dotenv").config()
const mongoose = require("mongoose")

const MongoDB = mongoose.connect(process.env.mongoDB, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
const ProductoShema = new mongoose.Schema({

    Nombre:{
        type:String,
        require : [true, "must provide a title"],
    },
    Precio: Number,
    Codigo: String,
    Descripcion :String,
    Categoria :String
})
const UserShema = new mongoose.Schema({
    username: {
        type:String,
        require : [true, "must provide a username"],
        minlength : [6, "username cant be less than 6 charactes"]
    },
})


const User = mongoose.model('User', UserShema);
const Producto = mongoose.model('Task', ProductoShema);

module.eeports ={
    MongoDB,
    Producto,
    User,
   
}