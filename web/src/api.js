async function fetchData(endpoint, queryParams = {}) {
    const queryString = Object.entries(queryParams)
      .map(([key, value]) => `${key}=${encodeURIComponent(value)}`)
      .join('&');
    
    const url = `${endpoint}${queryString ? `?${queryString}` : ''}`;
  
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`API request failed with status ${response.status}`);
    }
    const data = await response.json();
    return data;
  }
  
  export async function getArtists(limit) {
    return fetchData(`/api/v1/artists`, { limit });
  }
  
  export async function getTracks(limit) {
    return fetchData(`/api/v1/tracks`, { limit });
  }
  
  export async function getPlays(startDate, endDate) {
    return fetchData(`/api/v1/plays`, { start_date: startDate, end_date: endDate });
  }
  