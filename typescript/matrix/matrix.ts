class Matrix {
  public rows: number[][];
  public columns: number[][];

  constructor(s: string) {
    this.rows = [];
    this.columns = [];

    s.split("\n").forEach(row => {
      this.rows.push(row.split(" ").map(strN => parseInt(strN)));
    });

    const nRows = this.rows.length;
    const nColumns = this.rows[0].length;

    for(let i = 0; i < nColumns; i++) {
      const column: number[] = [];
      for(let j = 0; j < nRows; j++) {
        column.push(this.rows[j][i]);
      }
      this.columns.push(column);
    }

    console.log(this.rows);
    console.log(this.columns);
  }
}

export default Matrix
