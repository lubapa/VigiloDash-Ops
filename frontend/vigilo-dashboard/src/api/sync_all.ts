export async function updateAllVMs(): Promise<void> {
  const apiUrl = import.meta.env.VITE_API_URL;
  const response = await fetch(`${apiUrl}/metadata/sync_all`, {
    method: 'GET',
  });

  if (!response.ok) {
    throw new Error('Error al actualizar las máquinas virtuales');
  }
}
