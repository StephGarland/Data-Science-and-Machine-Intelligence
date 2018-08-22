using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using UnityEditor;
using UnityEngine;
using UnityEngine.UI;

public class RedGreenGradient : MonoBehaviour {

    public Button button;
    public Text outputText;

    public GameObject Robot_Model;
    private Animator robot_animator;

    public Slider slider;
    public Material material;
    public InputField mainInputField;
    Color redGreenGradient;
    private float currentSentiment;

    bool waitingOnAnalysis;
    int nPredictions;

    string current_opinion;

    // Use this for initialization
    void Start() {
        Debug.Log("Start...");
        waitingOnAnalysis = false;

        nPredictions = File.ReadAllLines(predictionFilePath).Length;
        Debug.Log("N Start Predictions: " + nPredictions);

        button.onClick.AddListener(TaskOnClick);
        robot_animator = Robot_Model.GetComponent<Animator>();
    }

    public void UpdateGradient(float x)
    {
        x = 1 - x;
        redGreenGradient = new Color(2.0f * x, 2.0f * (1 - x), 0);
        material.color = redGreenGradient;
    }

    // Update is called once per frame
    void Update() {
        if (waitingOnAnalysis)
        {
            if (WatchForResults())
                ResultsHaveReturned();
        }
            
    }

    private float randomFloat()
    {
        return UnityEngine.Random.Range(0.0f, 1.0f);
    }

    float timeToWait = 0.0001f;
    float fillQuantity = 0.005f;

    public void StartSlider()
    {
        StopAllCoroutines();
        StartCoroutine("FillSlider");
    }

    public IEnumerator FillSlider()
    {
        while (slider.normalizedValue != currentSentiment)
        {
            if (slider.normalizedValue <= currentSentiment)
                slider.normalizedValue += fillQuantity;
            if (slider.normalizedValue >= currentSentiment)
                slider.normalizedValue -= fillQuantity;

            UpdateGradient(slider.normalizedValue);
            yield return new WaitForSeconds(timeToWait);
        }
    }

    void setAnimationsToIdle()
    {
        robot_animator.SetBool("isAngry", false);
        robot_animator.SetBool("isHappy", false);
    }

    void TaskOnClick()
    {
        current_opinion = mainInputField.text;
        if (current_opinion != "")
        {
            //clear any ongoing animations:
            setAnimationsToIdle();

            WriteOpinionToFile(current_opinion);
            waitingOnAnalysis = true;

            mainInputField.text = "Updating...";
            //Calculate sentiment:
            //currentSentiment = randomFloat();
        }
    }

    private void ResultsHaveReturned()
    {
        //Get slider to move to sentiment pos
        StartSlider();

        mainInputField.text = current_opinion;
        //Print calculated sentiment to console:
        
        Debug.Log(currentSentiment.ToString());

        //Animate current sentiment
        if (currentSentiment <= 0.5f)
        {
            outputText.text = "Sentiment is NEGATIVE: " + currentSentiment.ToString();
            robot_animator.SetBool("isAngry", true);
        }
        else
        {
            outputText.text = "Sentiment is POSITIVE: " + currentSentiment.ToString();
            robot_animator.SetBool("isHappy", true);
        }
    }
    
    string opinionFilePath = @"C:\Users\GARLA\Documents\Sentiment Analysis\Showcase Demo\robotDemo_opinions.txt";
    string predictionFilePath = @"C:\Users\GARLA\Documents\Sentiment Analysis\Showcase Demo\robotDemo_predictions.txt"; 

    public void WriteOpinionToFile(string opinion)
    {
        string path = opinionFilePath;
        // This text is added only once to the file.
        if (!File.Exists(path))
        {
            // Create a file to write to.
            using (StreamWriter sw = File.CreateText(path))
            {
                sw.WriteLine("Opinion, Prediction, Actual");
            }
        }

        // This text is always added, making the file longer over time
        // if it is not deleted.
        using (StreamWriter sw = File.AppendText(path))
        {
            sw.WriteLine(opinion);
        }

        waitingOnAnalysis = true;
    }

    public bool WatchForResults()
    {
        if(nPredictions != File.ReadAllLines(predictionFilePath).Length)
        {
            Debug.Log("New Result Detected");
            nPredictions++;           
            currentSentiment = ReadLastPrediction();
            return true;
        }
        else
        {
            mainInputField.text += "*";
            return false;
        }
    }

    public float ReadLastPrediction()
    {
        // Open the file to read from.
        using (StreamReader sr = File.OpenText(predictionFilePath))
        {
            string lastLine = File.ReadAllLines(predictionFilePath).Last();
            Debug.Log(lastLine);
            waitingOnAnalysis = false;
            return float.Parse(lastLine);           
        }
    }
}



