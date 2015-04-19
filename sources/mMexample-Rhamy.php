<!DOCTYPE html>
<html>

<head>
    <title>Letter Case Modifier</title>
</head>

<body>
    <center>
        <section style="width: 50%;">
            <br />
            <br />
            <br />
            <h1>Welcome to the Letter Case Modifier</h1>
            <p>The program is designed to take the text in <a href='https://staff.fnwi.uva.nl/t.h.koornwinder/art/informal/KLSadd.tex' target='_blank'>KLSadd.tex</a> and <strong>inverse</strong> any letter's case that you choose. If you see red text below, either you haven't started or something went wrong; check your input and try again. In the end, a green "Finished" message will appear below and you may go and save <a href='https://www.tjhsst.edu/~2016rbelayac/NIST/KLSaddModified.tex' target='_blank'>KLSaddModified.tex</a> which will have the modification.</p>
            <br />
            <form name="inp" method="POST" action="changeLetterCase.php">
                <fieldset>
                    Text comes from the file <a href='https://staff.fnwi.uva.nl/t.h.koornwinder/art/informal/KLSadd.tex' target='_blank'>KLSadd.tex</a>

                    <br />
                    <br /> Choose a Letter to Inverse Case:
                    <br />
                    <select name="letterDrop">
                        <option value="">Select a Letter</option>
                        <option value="all">All</option>
                        <?php

						for($i = 97; $i < 123; $i++)
						{
						    echo "<option value=".chr($i).">".chr($i)."</option>";
						}

						?> 
                    </select>


                    <br />
                    <br />
                    <button type="submit" accesskey="s"><u>S</u>ubmit</button>
                </fieldset>
            </form>
            <br />
            <i>STATUS (wait for the green Finished Message):</i>
            <br />
            <br />

			<?php

			$content = file_get_contents('https://staff.fnwi.uva.nl/t.h.koornwinder/art/informal/KLSadd.tex');

			if($_POST['letterDrop'] != '' && preg_match("/^[a-z]$|^All$/i", $_POST['letterDrop'], $matches)) {
			  $letter = $_POST['letterDrop'];
			} else {
			  echo "<font color='red'>Please select valid letter from dropdown list.</font><br />";
			}

			$finString = "";

			if (stripos($content, $letter) !== FALSE && strlen($letter) !== 3) {
				$pattern = "/".$letter."/i";

				$finString = preg_replace_callback($pattern, function ($c) { return $c[0] ^ ' '; }, $content);
			} 
			else if (strlen($letter) == 3) {
				$finString = strtolower($content) ^ strtoupper($content) ^ $content;
			}
			else {
				echo "<font color='red'>The selected letter does not exist in the inputed text!</font>";
			}

			if (strlen($finString) > 0) {
				file_put_contents("KLSaddModified.tex", $finString);
				echo "<font color='green'>Finished, please check the file. Click here to view and save: <a href='https://www.tjhsst.edu/~2016rbelayac/NIST/KLSaddModified.tex' target='_blank'>KLSaddModified.tex</a></font>";
			}

			?>
			  
		</section>
	</center>
</body>
</html>