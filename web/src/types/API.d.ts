type SpotifyDetails = {
  playlists: SpotifyApi.PlaylistObjectSimplified[];
  artists: SpotifyApi.ArtistObjectFull[];
  tracks: SpotifyApi.TrackObjectFull[];
};

type SpotifySession = {
  session: string;
  name: string;
  id: string;
  uri: string;
  image?: {
    width?: number;
    height?: number;
    url: string;
  };
};

type SpotifyMediaPlay = {
  media: { track: SpotifyApi.TrackObjectFull; youtube: { id: string } };
  error: string;
};
