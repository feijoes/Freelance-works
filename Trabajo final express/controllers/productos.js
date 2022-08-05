const { Producto } = require('../db/coneccion');
const { AsyncWrapper } = require('../middlewares/middleware')

const GetAllProductos = AsyncWrapper( async (req,res)=>{
    const allProductos = await Producto.find()
    const changeProductos = allProductos.map(e=>{
        e.codigo = e._id;
        delete e._id
        return e
    })
    res.status(200).json({ changeProductos });
   
});

const PostProducto = AsyncWrapper( async ( req,res )=>{
    const newProducto = await Producto.create(req.body);
    res.status(201).json({ newProducto });
});


// Get , Modifying and Delete a task
const GetOneProducto = AsyncWrapper( async (req,res, next)=>{
    
    
    const producto = await Producto.findById({ _id:req.params.id  })

    if(!producto) {
        return next(CreateError(`no producto with id ${ req.params.id  }`, 404))
    }
    
    res.status(200).json({ producto })
});

module.exports= {
    GetAllProductos,
    PostProducto,
    GetOneProducto
}