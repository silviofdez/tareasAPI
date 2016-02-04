var express     =   require("express");
var app         =   express();
var bodyParser  =   require("body-parser");
var mongoOp     =   require("./models/tareas");
var router      =   express.Router();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({"extended" : false}));

router.get("/",function(req,res){
    res.json({"error" : false,"message" : "Bienvenido"});
});

router.route("/tareas")
    .get(function(req,res){
        var response = {};
        mongoOp.find({},function(err,data){
            if(err) {
                response = {"error" : true,"message" : "Error al recuperar datos"};
            } else {
                response = {"error" : false,"message" : data};
            }
            res.json(response);
        });
    })
    .post(function(req,res){
        var db = new mongoOp();
        var response = {};
        db.titulo = req.body.titulo;
        db.descripcion = req.body.descripcion;
        db.save(function(err){
            if(err) {
                response = {"error" : true,"message" : "Error insertando datos"};
            } else {
                response = {"error" : false,"message" : "Insercion correcta"};
            }
            res.json(response);
        });
    });

router.route("/tareas/:id")
    .get(function(req,res){
        var response = {};
        mongoOp.findById(req.params.id,function(err,data){
            if(err) {
                response = {"error" : true,"message" : "Error al recuperar datos"};
            } else {
                response = {"error" : false,"message" : data};
            }
            res.json(response);
        });
    })
    .put(function(req,res){
        var response = {};
        mongoOp.findById(req.params.id,function(err,data){
            if(err) {
                response = {"error" : true,"message" : "Error al recuperar datos"};
            } else {
                if(req.body.titulo !== undefined) {
                    data.titulo = req.body.titulo;
                }
                if(req.body.descripcion !== undefined) {
                    data.descripcion = req.body.descripcion;
                }
                data.save(function(err){
                    if(err) {
                        response = {"error" : true,"message" : "Error al actualizar datos"};
                    } else {
                        response = {"error" : false,"message" : "Datos actualizados:  "+req.params.id};
                    }
                    res.json(response);
                })
            }
        });
    })
    .delete(function(req,res){
        var response = {};
        mongoOp.findById(req.params.id,function(err,data){
            if(err) {
                response = {"error" : true,"message" : "Error al recuperar datos"};
            } else {
                mongoOp.remove({_id : req.params.id},function(err){
                    if(err) {
                        response = {"error" : true,"message" : "Error al borrar datos"};
                    } else {
                        response = {"error" : true,"message" : "Datos borrados: "+req.params.id};
                    }
                    res.json(response);
                });
            }
        });
    })

app.use('/',router);

app.listen(3000);
console.log("Servidor arrancado en el puerto 3000");
