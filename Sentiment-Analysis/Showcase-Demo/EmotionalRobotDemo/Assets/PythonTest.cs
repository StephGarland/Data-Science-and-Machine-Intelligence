using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using UnityEngine;

public class PythonTest : MonoBehaviour
{
    // Use this for initialization
    IEnumerator Start()
    {
        string url = "https://www.random.org/decimal-fractions/?num=1&dec=5&col=2&format=plain&rnd=new";
        using (WWW www = new WWW(url))
        {
            yield return www;
            UnityEngine.Debug.Log(www.text);
        }
    }


    // Update is called once per frame
    void Update()
    {

    }
}
