import React from 'react';
import styled from "styled-components";

class Signin extends React.Component{
  render(){

    var firebaseConfig = {
      apiKey: "AIzaSyByjZezt7xhRuwoKI_GPkYNCmehUCEZj5Q",
      authDomain: "singular-coil-302002.firebaseapp.com",
      projectId: "singular-coil-302002",
      storageBucket: "singular-coil-302002.appspot.com",
      messagingSenderId: "231493844645",
      appId: "1:231493844645:web:c34bf083786205043a174c",
      measurementId: "G-G62TPJMY23"
    };

  //Initialize Firebase
  firebase.initializeApp(firebaseConfig);

  function login() {
      var provider = new firebase.auth.GoogleAuthProvider();
      firebase.auth()
  .signInWithPopup(provider)
  .then((result) => {
    /** @type {firebase.auth.OAuthCredential} */
    var credential = result.credential;
  
    // This gives you a Google Access Token. You can use it to access the Google API.
    var token = credential.accessToken;
    // The signed-in user info.
    var user = result.user;
  
    console.log(token);
    // ...
  }).catch((error) => {
    // Handle Errors here.
    var errorCode = error.code;
    var errorMessage = error.message;
    // The email of the user's account used.
    var email = error.email;
    // The firebase.auth.AuthCredential type that was used.
    var credential = error.credential;
    // ...
    console.log(errorCode, errorMessage, credential)
  });
  }

    return(
      <div> 
        <script src='https://cdn.firebase.com/js/client/2.2.1/firebase.js'></script>
        <script src='https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js'></script>
        <script src="https://www.gstatic.com/firebasejs/4.1.3/firebase.js"></script>
        
        <div id="login_div" class="main-div">
        <centre>
        <h2 style="text-align:center;">Welcome to SeniorChat!</h2>
        </centre>
        <button onclick="login()">Login using Google</button>
        </div>

      </div>
    )
  }
}

export default Signin