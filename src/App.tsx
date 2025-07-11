import { Navbar } from '@/components/navbar';
import { Footer } from '@/components/footer';
import { Home } from '@/pages/home';

function App() {
  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      <main className="flex-grow">
        <Home />
      </main>
      <Footer />
    </div>
  );
}

export default App;
