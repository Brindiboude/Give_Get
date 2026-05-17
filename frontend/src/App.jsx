import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import Login from './pages/Login'
import Register from './pages/Register'
import Items from './pages/Items'
import CreateItem from './pages/CreateItem'

function App() {
  const token = localStorage.getItem('token')

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/items" element={token ? <Items /> : <Navigate to="/login" />} />
        <Route path="/create-item" element={token ? <CreateItem /> : <Navigate to="/login" />} />
        <Route path="*" element={<Navigate to={token ? "/items" : "/login"} />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
