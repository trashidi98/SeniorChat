import React from 'react';
import Test from "./Test"
import ContactCard from "./ContactCard";

function App(){

  const sayHello = () =>{
    console.log("hello"); 
  }; 
  const counter = 0; 
  console.log(counter);
  return(
    <div>
      <Test/>
      <ContactCard/>
      <h1>Hello React </h1>
      <button> hello </button>
      </div>
  );
}
export default App;
