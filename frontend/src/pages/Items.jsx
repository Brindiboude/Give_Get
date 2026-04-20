import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import api from '../services/api'

function Items() {
  const [items, setItems] = useState([])
  const [category, setCategory] = useState('')
  const [city, setCity] = useState('')
  const navigate = useNavigate()

  useEffect(() => {
    fetchItems()
  }, [])

  const fetchItems = async () => {
    try {
      const params = {}
      if (category) params.category = category
      if (city) params.city = city
      const res = await api.get('/items', { params })
      setItems(res.data)
    } catch (err) {
      console.error(err)
    }
  }

  const handleLogout = () => {
    localStorage.removeItem('token')
    navigate('/login')
  }

  return (
    <div style={{ maxWidth: '800px', margin: '20px auto', padding: '20px' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between' }}>
        <h1>Give_Get</h1>
        <button onClick={handleLogout}>Déconnexion</button>
      </div>

      <h2>Objets disponibles</h2>

      <div style={{ marginBottom: '20px' }}>
        <input
          type="text"
          placeholder="Filtrer par ville..."
          value={city}
          onChange={(e) => setCity(e.target.value)}
          style={{ marginRight: '10px' }}
        />
        <select value={category} onChange={(e) => setCategory(e.target.value)} style={{ marginRight: '10px' }}>
          <option value="">Toutes catégories</option>
          <option value="Vêtements">Vêtements</option>
          <option value="Livres">Livres</option>
          <option value="Électronique">Électronique</option>
          <option value="Sport & loisirs">Sport & loisirs</option>
          <option value="Maison & déco">Maison & déco</option>
          <option value="Autres">Autres</option>
        </select>
        <button onClick={fetchItems}>Filtrer</button>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '20px' }}>
        {items.map(item => (
          <div key={item.id} style={{ border: '1px solid #ccc', padding: '15px', borderRadius: '8px' }}>
            <h3>{item.title}</h3>
            <p>{item.description}</p>
            <p><strong>Catégorie :</strong> {item.category}</p>
            <p><strong>État :</strong> {item.condition}</p>
            {item.city && <p><strong>Ville :</strong> {item.city}</p>}
          </div>
        ))}
      </div>

      {items.length === 0 && <p>Aucun objet disponible pour le moment.</p>}
    </div>
  )
}

export default Items
