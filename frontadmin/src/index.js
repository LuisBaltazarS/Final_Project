
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Usuarios from './components/usuarios';
import Directores from './components/directores';
import Tutores from './components/tutores';
import Tipos from './components/tipos';
import { Route, Link, Routes, BrowserRouter as Router } from 'react-router-dom'
import App from './App';
import Notfound from './components/notfound';
import reportWebVitals from './reportWebVitals';

const routing = (
  <Router>
    <div className="container">
      <header className="d-flex justify-content-center py-3">
        <ul className="nav nav-pills">
            <li className="nav-item"><Link to="/" className="nav-link active" aria-current="page">Inicio</Link></li>
            <li className="nav-item"><Link to="/usuarios" className="nav-link" aria-current="page">Usuarios</Link></li>
            <li className="nav-item"><Link to="/tutores" className="nav-link" aria-current="page">Tutores</Link></li>
            <li className="nav-item"><Link to="/directores" className="nav-link" aria-current="page">Directores</Link></li>
            <li className="nav-item"><Link to="/tipos" className="nav-link" aria-current="page">Tipos Usuarios</Link></li>
        </ul>
      </header>
      <hr></hr>
    </div>
    
    <div className="container py-2 px-5">
        <Routes>
          <Route exact path="/" element={<App/>}/>
          <Route path="/usuarios" element={<Usuarios />} />
          <Route path="/tutores" element={<Tutores />} />
          <Route exact path="/directores" element={<Directores/>}/>
          <Route exact path="/tipos" element={<Tipos/>}/>
          <Route path="*" element={<Notfound/>} />
        </Routes>
    </div>
  </Router>
)
ReactDOM.render(routing, document.getElementById('root'))

reportWebVitals();
