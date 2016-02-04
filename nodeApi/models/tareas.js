var mongoose    =   require("mongoose");
mongoose.connect('mongodb://localhost:27017/tareasDb');
var mongoSchema =   mongoose.Schema;
var tareasSchema  = {
    "titulo" : String,
    "descripcion" : String
};
module.exports = mongoose.model('tareas',tareasSchema);;
