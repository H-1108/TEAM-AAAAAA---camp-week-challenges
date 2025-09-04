import java.nio.file.{Files, Paths}
import java.nio.charset.StandardCharsets

object Main {
  def main(args: Array[String]): Unit = {
    val inputPath  = if (args.length >= 1) args(0) else "data6.txt"
    val outputPath = if (args.length >= 2) args(1) else "data7.txt"

    val src   = scala.io.Source.fromFile(inputPath)
    val lines = try src.getLines().toList finally src.close()

    val outputLines = lines.zipWithIndex.map {
      case (line, idx) if idx == 0 =>
        s"$line,Comments"

      case (line, _) =>
        // keep empty fields by using -1
        val parts = line.split(",", -1)
        if (parts.length < 9) {
          s"$line,"
        } else {
          val summary    = parts(7).trim
          val evaluation = toFloatSafe(parts(8))

          val comments =
            if (summary == "super" && evaluation >= 3.0f) "Excellent"
            else if (summary == "super")                  "Good but inconsistent"
            else if (evaluation >= 2.0f)                  "Promising"
            else                                          "Needs Improvement"

          s"$line,$comments"
        }
    }

    Files.write(
      Paths.get(outputPath),
      outputLines.mkString("\n").getBytes(StandardCharsets.UTF_8)
    )
  }

  private def toFloatSafe(s: String): Float =
    try s.trim.toFloat
    catch { case _: Throwable => Float.NaN }
}
