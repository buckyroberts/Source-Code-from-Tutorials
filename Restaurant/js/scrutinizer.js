var aaharvihar = angular.module('restaurent',["ngRoute"]);

aaharvihar.config(function($routeProvider){
    $routeProvider
    .when("/",{
        templateUrl:"main.html"
    })
    .when("/login",{
        templateUrl :"login.html"
    })
    .when("/signup",{
        templateUrl:"signup.html"
    })
    .when("/foodItems",{
        templateUrl:"homepage.html"
    })
    .when("/main",{
        templateUrl:"table.html"
    })
    .when("/Analytics6",{
        templateUrl:"Analytics.html"
    })
});


aaharvihar.controller('onlineOrder',function($scope,$http,$window,AaharViharService,$rootScope){

  //  $scope.newMessage =AaharViharService.setMessage("Helllo i am the user");
    $scope.welcome_Msg = AaharViharService.getWelcomeMsg();


    $scope.login = function(){
        alert('entering  to  login ');
        $window.location.href="#!login";
    };

    $scope.signup = function(){
        alert('entering to signup');
        $window.location.href="#!signup";
    };
    $scope.search = function(){
            alert('table');
        $window.location.href="#!userInfo"
    };
    $scope.search = function(){
        alert('Analytics6');
        $window.location.herf="#!Analytics6"
    };



});

aaharvihar.controller('security',function($scope,$http,$window,AaharViharService,$rootScope){
    $scope.submit= function(){
        if($scope.emailid != undefined && $scope.password != undefined){
            $http.get('http://localhost:4001/login?emailid=' +$scope.emailid+ '&password='+$scope.password)
            .then(function(res){
                if(res.data.code==200){
                    alert('order your food');
                    AaharViharService.getData().then(function(res,req){
                        if(res!=null){
                           $rootScope.myData = res.data;
                           $window.location.href="#!foodItems";
                         }
                       }).catch(function(err){
                         console.log("Error");
                       })

                    //$window.location.href="#!main";
                }
                else{
                    alert('please enter correct details');
                }
            })
            .catch(function(err){
                alert('you dont have account on this userid or number')
                alert('please create a new account')
                $window.location.href="#!signup";

            })
        }
        else{
            alert('please enter the details');
        }
    }


    $scope.enter=function(){

        if($scope.username != undefined && $scope.emailid != undefined  && $scope.mobilenumber != undefined && $scope.password == $scope.repassword){

        $http.post('http://localhost:4001/signup',{
            "username":$scope.username,
            "emailid":$scope.emailid,
            "mobilenumber":$scope.mobilenumber,
            "password":$scope.password
        })
        .then(function(response){
            console.log(response)
            if(response.data.code==200){
                alert('sucess fully stored')
                alert('order your tasty food ');
              /**    document.getElementById("emailid").value = "";
                    document.getElementById("password").value = ""; **/
            }
            else{
                alert('check your mongodb')
            }
        })
        .catch(function(error){
            console.log(error);
            alert('sever problem')
        })
    }
        else
            {
                alert('please enter all details')
            }
    }
});







aaharvihar.factory('AaharViharService',function($http,$q){
    return {
    getWelcomeMsg: function() {
        return "Welcome to ML Labs";
    },
    getData: function(){
        console.log("Getdata");
        return $http.get('http://localhost:4001/userInfo');
        }
      }
});


