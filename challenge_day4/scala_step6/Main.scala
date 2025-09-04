import java.nio.file.{Files, Paths}
import java.nio.charset.StandardCharsets

object Main {
  def main(args: Array[String]): Unit = {
    // Default to fulldata paths; CLI args still override if provided
    val defaultIn  = "../fulldata/data6.txt"
    val defaultOut = "../fulldata/data7.txt"

    val inputPath  = if (args.length >= 1) args(0) else defaultIn
    val outputPath = if (args.length >= 2) args(1) else defaultOut

    val src   = scala.io.Source.fromFile(inputPath)
    val lines = try src.getLines().toList finally src.close()

    val outputLines = lines.zipWithIndex.map {
      case (line, idx) if idx == 0 => s"$line,Comments"
      case (line, _) =>
        val parts = line.split(",", -1)
        if (parts.length < 9) s"$line,"
        else {
          val summary    = parts(7).trim
          val evaluation = toFloatSafe(parts(8))
          val comments =
            if (summary == "super" && evaluation.exists(_ >= 3.0f)) "Excellent"
            else if (summary == "super")                             "Good but inconsistent"
            else if (evaluation.exists(_ >= 2.0f))                    "Promising"
            else                                                      "Needs Improvement"
          s"$line,$comments"
        }
    }

    Files.write(
      Paths.get(outputPath),
      outputLines.mkString("\n").getBytes(StandardCharsets.UTF_8)
    )
    println(s"[OK] Wrote: $outputPath")
  }

  private def toFloatSafe(s: String): Option[Float] =
    try Some(s.trim.toFloat) catch { case _: Throwable => None }
}
