import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import api from '../services/api'

function CreateItem() {
  const [form, setForm] = useState({
    title: '',
    description: '',
    category: '',
    condition: '',
    size: '',
    city: ''
  })
  const [error, setError] = useState('')
  const navigate = useNavigate()

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      await api.post('/items', form)
      navigate('/items')
    } catch (err) {
      setError('Erreur lors de la création de l\'objet')
    }
  }

  return (
    <div style={{ maxWidth: '500px', margin: '40px auto', padding: '20px' }}>
      <h1>Give_Get</h1>
      <h2>Publier un objet</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <label>Titre *</label>
          <input
            type="text"
            name="title"
            value={form.title}
            onChange={handleChange}
            required
            style={{ display: 'block', width: '100%', marginBottom: '10px' }}
          />
        </div>
        <div>
          <label>Description</label>
          <textarea
            name="description"
            value={form.description}
            onChange={handleChange}
            style={{ display: 'block', width: '100%', marginBottom: '10px' }}
          />
        </div>
        <div>
          <label>Catégorie *</label>
          <select
            name="category"
            value={form.category}
            onChange={handleChange}
            required
            style={{ display: 'block', width: '100%', marginBottom: '10px' }}
          >
            <option value="">Choisir une catégorie</option>
            <option value="Vêtements">Vêtements</option>
            <option value="Livres">Livres</option>
            <option value="Électronique">Électronique</option>
            <option value="Sport & loisirs">Sport & loisirs</option>
            <option value="Maison & déco">Maison & déco</option>
            <option value="Autres">Autres</option>
          </select>
        </div>
        <div>
          <label>État *</label>
          <select
            name="condition"
            value={form.condition}
            onChange={handleChange}
            required
            style={{ display: 'block', width: '100%', marginBottom: '10px' }}
          >
            <option value="">Choisir un état</option>
            <option value="neuf">Neuf</option>
            <option value="très bon état">Très bon état</option>
            <option value="bon état">Bon état</option>
            <option value="état correct">État correct</option>
          </select>
        </div>
        <div>
          <label>Taille (optionnel)</label>
          <input
            type="text"
            name="size"
            value={form.size}
            onChange={handleChange}
            style={{ display: 'block', width: '100%', marginBottom: '10px' }}
          />
        </div>
        <div>
          <label>Ville</label>
          <input
            type="text"
            name="city"
            value={form.city}
            onChange={handleChange}
            style={{ display: 'block', width: '100%', marginBottom: '10px' }}
          />
        </div>
        <button type="submit">Publier</button>
        <button type="button" onClick={() => navigate('/items')} style={{ marginLeft: '10px' }}>
          Annuler
        </button>
      </form>
    </div>
  )
}

export default CreateItem
