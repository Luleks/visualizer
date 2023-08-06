using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Serialization;
using System.Xml;
using System.IO;



namespace Settings
{
    [Serializable]
    public class ArraySettings
    {
		#region Enums
		public enum ArrayType { Static, Dynamic };
        public enum SortingAlg { Bubble, Insertion, Selection };
		#endregion

		#region Attrs
		private ArrayType arrayType;
        private int arraySize;
        private SortingAlg sortingAlg;
		#endregion

		#region Properties
        public ArrayType array_type
        {
            get { return arrayType; }
            set { arrayType = value; }
        }

        public int array_size
        {
            get { return arraySize; }
            set { arraySize = value; }
        }

        public SortingAlg sorting_alg
        {
            get { return sortingAlg; }
            set { sortingAlg = value; }
        }
		#endregion


		public ArraySettings()
        {
            arrayType = ArrayType.Static;
            arraySize = 4;
            sortingAlg = SortingAlg.Bubble;
        }

        public ArraySettings(ArrayType atype, int asize, SortingAlg sortingAlg)
        {
            arrayType = atype;
            arraySize = asize;
            this.sortingAlg = sortingAlg;
        }

        public void SaveAsXML(string filename)
        {
            using (XmlTextWriter tw = new XmlTextWriter(filename, Encoding.ASCII))
            {
                tw.Formatting = Formatting.Indented;
                XmlSerializer xsr = new XmlSerializer(typeof(ArraySettings));
                xsr.Serialize(tw, this);
            }
        }

        public static ArraySettings LoadFromXml(string filename)
        {
            using (StreamReader sr = new StreamReader(filename, Encoding.ASCII))
            {
                XmlSerializer xsr = new XmlSerializer(typeof(ArraySettings));
                ArraySettings array_settings = (ArraySettings)xsr.Deserialize(sr);
                return array_settings;
            }
        }

        

    }
}
