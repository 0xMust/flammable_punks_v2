import './App.css';
import Minter from './Minter'
import background from './out.gif'
import { UrlJsonRpcProvider } from '@ethersproject/providers';

function App() {
  return (
    <div className="App" style={{
      backgroundImage: `url(${background})`,
      //backgroundRepeat: 'no-repeat',
      backgroundSize: '100% 100%',
      height: '100vh'
    }}>
      <Minter></Minter>
    </div>
  );
}

export default App;
