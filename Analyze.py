import pandas as pd
import matplotlib.pyplot as plt
import os

def analyze_results(filename):
    filepath = f"Results/{filename}"
    if not os.path.exists(filepath):
        print(f"Filen {filename} hittades inte.")
        return

    # 1. Ladda data
    df = pd.read_csv(filepath)

    # 2. Gruppera data per iteration
    # Vi tar alla 100 batches och räknar ut snitt/std för varje iteration (1-500)
    summary = df.groupby('Iteration')['Time_ns'].agg(['mean', 'std']).reset_index()

    # Konvertera nanosekunder till millisekunder för att göra det mer läsbart i grafer
    summary['mean_ms'] = summary['mean'] / 1_000_000
    summary['std_ms'] = summary['std'] / 1_000_000

    # 3. Skapa grafen
    plt.figure(figsize=(12, 6))
    
    # Plotta medelvärdet
    plt.plot(summary['Iteration'], summary['mean_ms'], color='blue', label='Genomsnittlig tid (ms)')
    
    # Skapa ett skuggat område för standardavvikelsen (osäkerhetsmarginalen)
    plt.fill_between(summary['Iteration'], 
                     summary['mean_ms'] - summary['std_ms'], 
                     summary['mean_ms'] + summary['std_ms'], 
                     color='blue', alpha=0.2, label='Standardavvikelse')

    # 4. Formatera grafen
    plt.title(f"Prestandaanalys: {filename.replace('_full.csv', '')}", fontsize=14)
    plt.xlabel("Iteration (Nr i ordningen)", fontsize=12)
    plt.ylabel("Tid (ms)", fontsize=12)
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.legend()

    # 5. Räkna ut "Steady State" (Jämviktsläget)
    # Vi antar att de sista 20% av körningarna har stabiliserat sig
    steady_state_df = summary.tail(int(len(summary) * 0.2))
    steady_avg = steady_state_df['mean_ms'].mean()
    
    print(f"\n--- Resultat för {filename} ---")
    print(f"Snitt i jämviktsläge: {steady_avg:.4f} ms")
    print(f"Max tid (ofta första körningen): {summary['mean_ms'].max():.4f} ms")
    print(f"Min tid: {summary['mean_ms'].min():.4f} ms")

    plt.show()

def main():
    mode = "Python"      # "Python", "Numpy", "Java"
    algo = "Quick"     # "Quick", "Merge", "mMtrix"
    data_size = "50"  # "50", "800", "5000"
    filename = mode + "_" + algo + "_" + data_size + "_full.csv"
    analyze_results(filename)