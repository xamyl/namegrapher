import os
from typing import Dict, Optional
import matplotlib.pyplot as plt
from pathlib import Path


class NameAnalyzer:
    """Analyzes the historical popularity of names from SSA dataset."""

    def __init__(self, directory: str | Path):
        """
        Initialize the NameAnalyzer with the directory containing name data files.

        Args:
            directory: Path to the directory containing SSA name files
        """
        self.directory = Path(directory)
        if not self.directory.exists():
            raise ValueError(f"Directory not found: {self.directory}")

    def get_name_popularity(self, name: str, gender: str) -> Dict[int, int]:
        """
        Get the popularity of a name across years.

        Args:
            name: The name to search for
            gender: 'M' for male or 'F' for female

        Returns:
            Dictionary mapping years to number of occurrences

        Raises:
            ValueError: If gender is invalid
        """
        if gender.upper() not in {'M', 'F'}:
            raise ValueError("Gender must be 'M' or 'F'")

        popularity = {}
        name = name.lower()
        gender = gender.upper()

        try:
            for file in sorted(self.directory.glob("yob*.txt")):
                if not file.name.startswith("yob") or not file.name.endswith(".txt"):
                    continue
                    
                year = int(file.name[3:7])
                
                with open(file, 'r', encoding='utf-8') as f:
                    for line in f:
                        data = line.strip().split(',')
                        if data[0].lower() == name and data[1] == gender:
                            popularity[year] = int(data[2])
                            break

        except (OSError, ValueError) as e:
            raise RuntimeError(f"Error processing name files: {e}")

        return popularity

    def plot_popularity(
        self,
        popularity: Dict[int, int],
        name: str,
        figsize: tuple[int, int] = (10, 6),
        color: str = 'blue',
        style: str = 'o-'
    ) -> None:
        """
        Plot the popularity of a name over time.

        Args:
            popularity: Dictionary mapping years to occurrences
            name: The name being plotted
            figsize: Tuple of (width, height) for the plot
            color: Color of the plot line
            style: Style of the plot line
        """
        if not popularity:
            raise ValueError(f"No data available for name '{name}'")

        years = sorted(popularity.keys())
        counts = [popularity[year] for year in years]

        plt.figure(figsize=figsize)
        plt.plot(years, counts, style, color=color)
        plt.title(f"Popularity of the Name '{name}' Over Time", fontsize=16)
        plt.xlabel("Year", fontsize=14)
        plt.ylabel("Number of Occurrences", fontsize=14)
        plt.grid(True)
        plt.tight_layout()
        plt.show()


def main():
    """Main function to run the name popularity analysis."""
    try:
        directory = Path(r"THISISIMPORTANTCHANGME")
        analyzer = NameAnalyzer(directory)

        name = input("Enter the name to search for: ").strip()
        if not name:
            print("Name cannot be empty.")
            return

        gender = input("Enter the gender (M/F): ").strip().upper()
        if gender not in {'M', 'F'}:
            print("Invalid gender. Please enter 'M' or 'F'.")
            return

        popularity = analyzer.get_name_popularity(name, gender)
        if popularity:
            analyzer.plot_popularity(popularity, name)
        else:
            print(f"The name '{name}' was not found in the dataset.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
