import { useState } from 'react';
import { updateAllVMs } from '../api/sync_all';

function UpdateAllButton() {
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');

  const handleClick = async () => {
    setLoading(true);
    setMessage('');
    try {
      await updateAllVMs();
      setMessage('Actualización completada.');
    } catch (err) {
      setMessage('Error al actualizar.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <button onClick={handleClick} disabled={loading}>
        {loading ? 'Actualizando...' : 'Actualizar Datos'}
      </button>
      {message && <p>{message}</p>}
    </div>
  );
}

export default UpdateAllButton;
