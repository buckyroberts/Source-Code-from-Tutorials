// NODE JS SERVICES //
var express_R = require('express');
var path_R = require('path');

var bodyParser_R = require('body-parser');

// mongoose schema 16/11/19
var mongoose = require('mongoose');
console.log(mongoose);

var schemaObj =mongoose.Schema;

var userSchema = new schemaObj({
    username : String,
    password : String,
});

console.log(userSchema);

var mongodb_R = require('mongodb').MongoClient;
mongodb_url = "mongodb://localhost:27017/test";

app = express_R();
app.use(bodyParser_R.urlencoded({
    extended : false
}))
app.use(bodyParser_R.json());


app.use(express_R.static(path_R.join(__dirname,'js')));
app.use (express_R.static(path_R.join(__dirname,'Analytics6')));
app.use(express_R.static(path_R.join(__dirname,'css')));
app.use(express_R.static(path_R.join(__dirname,'view')));



app.get('/',function(req,res){
    res.sendFile("E:\\Restaurant\\view\\index.html");
});


app.post('/signup',function(request,response){

    console.log('collecting the data and storeing into db');
    response.setHeader('content-type','text/plain');

    mongodb_R.connect(mongodb_url,function(err,db){

        if(err){
            console.log(err);
            console.log('please check with your mongodb server(on/off)');
        }
        else{
            console.log(db);
            var db_R = db.db('aaharvihar');
            var collection_R = db_R.collection('userData')

            json_data = {
                "username":request.body.username,
                "emailid":request.body.emailid,
                "mobile":request.body.mobilenumber,
                "password":request.body.password
            }
            collection_R.insertOne(json_data);
            console.log('Welcome to MlLabs....please experince our Wao Factor')
            response.jsonp({"code":200,"message":"User Data Inserted Successfully"})


        }

    })
});

app.get('/login',function(req,res){

    console.log('please enter your details')

    mongodb_R.connect(mongodb_url,function(err,db){
        if(err){
            throw err;
            console.log('please check with your mongodb server');
        }
        else{

            var db_R = db.db("aaharvihar");

            var json_data = {

                "emailid": req.query.emailid,
                "password": req.query.password
            }
            db_R.collection('userData').findOne(json_data,function(error,response){
                if(err){
                    throw err;


                    console.log('your database is not found');
                }
                else{
                    if(res == null){

                        console.log('your details is not found......kindly please check with your user id and password');
                    }
                    else{
                        console.log(res);
                        console.log('Congrats...Welcome  to ML labs');
                        res.jsonp({code:200,message:"Login Successful"})
                    }
                }
            })
        }
    })
});


app.get('/userInfo',function(req,res){

    console.log("\n******* Inside userinfo ********");

    mongodb_R.connect(mongodb_url, function(err,db){
        if(err){
            throw err;
            console.log('please check with your mongodb server');

        }
        else{
            var db_R = db.db("aaharvihar");
            var userDetails=[];
            db_R.collection("userData").find({}).toArray(function(err,result){
                if (err) throw err;
                res.jsonp(result);
                db.close();
            });

    }
    });
});



console.log('*****entering into page');
app.listen(4001);
