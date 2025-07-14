import { useEffect, useState } from 'react';
import UpdateAllButton from './components/UpdateAllButton';
interface VM {
  id: string;
  name: string;
  status: string;
  client: string;
  owner: string;
}

function Dashboard() {
  const apiUrl = import.meta.env.VITE_API_URL;
  const [items, setItems] = useState<VM[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Obtener datos de la API
  useEffect(() => {
    fetch(`${apiUrl}/metadata/`)
      .then(res => {
        if (!res.ok) throw new Error('Error al cargar Metadata');
        return res.json();
      }) 
      .then((data: Record<string, Omit<VM, 'id'>>) => {
        // Convertir objeto en array con id incluido
        const list = Object.entries(data).map(([id, info]) => ({ id, ...info }));
        setItems(list);
        setLoading(false);
      })
      .catch((err: unknown) => {
        if (err instanceof Error) setError(err.message);
        else setError(String(err));
        setLoading(false);
      });
  }, [apiUrl]);

  if (loading) return <p>Cargando Maquinas Virtuales...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div style={{ padding: '1rem' }}>
      <h1>Dashboard de Máquinas Virtuales</h1>
      <table border={1} cellPadding={10}>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Estado</th>
            <th>Cliente</th>
            <th>Owner</th>
          </tr>
        </thead>
        <tbody>
          {items.map(vm => (
            <tr key={vm.id}>
              <td>{vm.id}</td>
              <td>{vm.name}</td>
              <td>{vm.status}</td>
              <td>{vm.client}</td>
              <td>{vm.owner}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <div>
      <UpdateAllButton />
      </div>
    </div>
   
  );
}

export default Dashboard;
