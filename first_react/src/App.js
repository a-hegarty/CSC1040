import './App.css';
import Favourite from './pages/favourites';
import Home from './pages/home';
import React from 'react'; 
import { Routes, Route } from 'react-router-dom';
import Navbar from './components/navbar';

function App() {

  return (
    <div>
      <Navbar/>
      <main className='main_content'>
        <Routes>
          <Route path='/' element={<Home/>}/>
          <Route path='/favourites' element={<Favourite/>}/>
        </Routes>
      </main>
    </div>
  );
}


 
export default App;
