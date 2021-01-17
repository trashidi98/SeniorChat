import React from 'react';
import ContactCard from "./ContactCard";
import Sidebar from './Test'
const items = [
  {name: 'home', label:'Home'},
  {name: 'searching', label:'Searching'},
  {name: 'profile', label: 'Profile'}, 
  {name: 'setting', label: 'Setting'}, 
]

function App(){

  const sayHello = () =>{
    console.log("hello"); 
  }; 
  const counter = 0; 
  console.log(counter);
  return(
    <div>
      <ContactCard/>
      <Sidebar items = {items} />
      <h1>Hello React </h1>
      <button> hello </button>
      </div>
  );
}
export default App;
