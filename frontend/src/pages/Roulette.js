import React, { useState } from "react";
import './Roulette.css';
import apple from './assets/apple.png';
import banana from "./assets/banana.png";
import grape from "./assets/grape.png";
import pumpkin from "./assets/pumpkin.png";
import meat from "./assets/meat.png";
import carrot from "./assets/carrot.png";
import steak from "./assets/steak.png";
import chicken from "./assets/chicken.png";
import fish from "./assets/fish.png";

const options = ['Select', 'Meat', 'Seafood', 'Fruit', 'Vegetables'];
const imageOptions = [banana, grape, pumpkin, meat, carrot, steak, chicken, fish, apple];

const Roulette = () => {
  const [selection1, setSelection1] = useState(options[0]);
  const [selection2, setSelection2] = useState(options[0]);
  const [selection3, setSelection3] = useState(options[0]);

  const [currentImage, setCurrentImage] = useState(apple);

  const handleSpin = () => {
    let counter = 0;
    const interval = setInterval(() => {
      setCurrentImage(imageOptions[Math.floor(Math.random() * imageOptions.length)]);

      counter++;
      if (counter > 10) {
        clearInterval(interval);
        setCurrentImage(apple);
      }
    }, 100);
  };

  return (
    <div className="container">
      <h1 className="title">Test Your Luck</h1>
      <div className="boxes-container">
        <div className="box-container">
          <div className="box">
            <img src={currentImage} alt="Slot" />
          </div>
          <div class="select-wrapper">
            <select class="drop-down" value={selection1} onChange={e => setSelection1(e.target.value)}>
              {options.map(option => (
                <option key={option} value={option}>{option}</option>
              ))}
            </select>
          </div>
        </div>

        <div className="box-container">
          <div className="box">
            <img src={currentImage} alt="Slot" />
          </div>
          <div class="select-wrapper">
            <select class="drop-down" value={selection1} onChange={e => setSelection2(e.target.value)}>
              {options.map(option => (
                <option key={option} value={option}>{option}</option>
              ))}
            </select>
          </div>
        </div>

        <div className="box-container">
          <div className="box">
            <img src={currentImage} alt="Slot" />
          </div>
          <div class="select-wrapper">
            <select class="drop-down" value={selection1} onChange={e => setSelection3(e.target.value)}>
              {options.map(option => (
                <option key={option} value={option}>{option}</option>
              ))}
            </select>
          </div>
        </div>
      </div>
      
      <button onClick={handleSpin} className="spinButton">Spin</button>
    </div>
  );
};

export default Roulette;