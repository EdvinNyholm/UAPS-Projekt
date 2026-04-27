import pandas as pd
import matplotlib.pyplot as plt
import os

# För att undvika att Ubuntu försöker öppna ett fönster
import matplotlib
matplotlib.use('Agg') # Detta tvingar fram en "non-interactive" backend

def analyze_results(filename):
    filepath = f"Results/{filename}"
    if not os.path.exists(filepath):
        print(f"❌ Fel: Filen {filename} hittades inte.")
        return

    # 1. Ladda data
    df = pd.read_csv(filepath)

    # 2. Gruppera data per iteration
    summary = df.groupby('Iteration')['Time_ns'].agg(['mean', 'std']).reset_index()

    summary['mean_ms'] = summary['mean'] / 1_000_000
    summary['std_ms'] = summary['std'] / 1_000_000

    # 3. Skapa grafen
    plt.figure(figsize=(12, 6))
    
    plt.plot(summary['Iteration'], summary['mean_ms'], color='#1f77b4', linewidth=2, label='Genomsnittlig tid (ms)')
    plt.fill_between(summary['Iteration'], 
                     summary['mean_ms'] - summary['std_ms'], 
                     summary['mean_ms'] + summary['std_ms'], 
                     color='#1f77b4', alpha=0.2, label='Standardavvikelse')

    # 4. Formatera grafen
    clean_name = filename.replace('_full.csv', '').replace('_', ' ')
    plt.title(f"Prestandaanalys: {clean_name}", fontsize=14, fontweight='bold')
    plt.xlabel("Iteration (Nr i ordningen)", fontsize=12)
    plt.ylabel("Tid (ms)", fontsize=12)
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.legend()

    # 5. Räkna ut statistik för rapporten
    steady_state_df = summary.tail(int(len(summary) * 0.2))
    steady_avg = steady_state_df['mean_ms'].mean()
    start_avg = summary['mean_ms'].iloc[0] # Kall start
    
    print("-" * 40)
    print(f"STATISTIK FÖR {clean_name.upper()}")
    print(f"Kall start:        {start_avg:.4f} ms")
    print(f"Jämviktsläge:      {steady_avg:.4f} ms")
    print("-" * 40)

    # --- HÄR ÄR ÄNDRINGEN FÖR UBUNTU ---
    # Skapa mappen 'Plots' om den inte finns
    if not os.path.exists("Plots"):
        os.makedirs("Plots")
        
    # Skapa ett snyggt filnamn och spara bilden
    plot_name = filename.replace("_full.csv", ".png")
    plot_path = os.path.join("Plots", plot_name)
    plt.savefig(plot_path)
    
    # Stäng figuren så att vi inte fyller minnet
    plt.close()
    
    print(f"✅ Grafen har sparats i: {plot_path}")

def main():
    mode = "Python"      # "Python", "Numpy", "Java"
    algo = "Merge"     # "Quick", "Merge", "Matrix"
    data_size = "5000"  # "50", "800", "1000"
    
    # Se till att case matchar precis vad Measure.py sparar
    filename = f"{mode}_{algo}_{data_size}_full.csv"
    analyze_results(filename)

if __name__ == "__main__":
    main()